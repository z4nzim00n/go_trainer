const fs = require("fs");
const path = require("path");

const SPEC_DIR = "specs";
const OUT_DIR = "tasks";

function parseSpecs(text) {
	const tasks = [];
	const lines = text.split(/\r?\n/);
	let task = null;
	let field = null;
	let buffer = [];

	function flush() {
		if (!task || !field) return;
		task[field] = buffer.join("\n").replace(/\s+$/, "");
		buffer = [];
	}

	for (const line of lines) {
		if (line.startsWith("@@")) {
			flush();
			field = null;

			if (line === "@@TASK") {
				if (task) throw new Error("previous task not closed with @@END");
				task = {};
				continue;
			}
			if (line === "@@END") {
				if (!task) throw new Error("@@END without @@TASK");
				tasks.push(task);
				task = null;
				continue;
			}
			if (!task) throw new Error("field outside task: " + line);
			field = line.slice(2).trim().toLowerCase();
			continue;
		}

		if (field === null && task) {
			const m = /^([a-zA-Z]+):\s?(.*)$/.exec(line);
			if (m) {
				task[m[1]] = m[2];
				continue;
			}
			if (line.trim() === "") continue;
			throw new Error("bad header line: " + line);
		}

		buffer.push(line);
	}

	return tasks;
}

function write(file, content) {
	fs.mkdirSync(path.dirname(file), { recursive: true });
	fs.writeFileSync(file, content.replace(/\r\n/g, "\n").replace(/\s+$/, "") + "\n");
}

function readme(t) {
	const examples = t.examples.replace(
		/^\|\s*Входные данные\s*\|\s*Результат работы\s*\|\r?\n\|[\s\-|]+\|\r?\n/,
		""
	);
	return [
		"## " + t.title,
		"",
		"### Задание",
		"| " + t.title.split(".")[0] + " ||",
		"| ------ | ------- |",
		"| **Темы:** | " + t.topics + " |",
		"| **Файл решения:** | main.go |",
		"| **Входные данные:** | " + t.input + " |",
		"| **Выходные данные** | Стандартный поток вывода (stdout) |",
		"",
		t.desc,
		"",
		"### Примеры",
		"",
		"| Входные данные | Результат работы |",
		"| ------ | ------ |",
		examples,
		"",
		"### Как проверить",
		"",
		"```bash",
		"bash " + t.run + ".sh",
		"```",
		""
	].join("\n");
}

function theory(t) {
	return "# Разбор задания\n\n" + t.theory + "\n";
}

function tests(t) {
	return [
		"# " + t.title + " — Тесты",
		"",
		"## Компиляция",
		"",
		"```bash",
		"go build -o app.exe main.go",
		"./app.exe",
		"```",
		"",
		"Эталон:",
		"",
		"```bash",
		"go run solution.go",
		"go run solution_commented.go",
		"```",
		"",
		"## Проверка вывода",
		"",
		"| Вход | Результат |",
		"| --- | --- |",
		t.tests,
		"",
		"## Автотесты",
		"",
		"```bash",
		"bash " + t.run + ".sh",
		"```",
		""
	].join("\n");
}

function runner(t) {
	return [
		"#!/usr/bin/env bash",
		"set -e",
		'cd "$(dirname "$0")"',
		"source ../../../scripts/lib.sh",
		"",
		"compile",
		"",
		t.cases,
		"",
		'if [ -z "$FAILED" ]; then',
		'  echo "Все тесты пройдены"',
		"else",
		'  echo "Есть проваленные тесты"',
		"  exit 1",
		"fi",
		""
	].join("\n");
}

const files = fs.readdirSync(SPEC_DIR).filter(f => f.endsWith(".spec")).sort();
if (files.length === 0) throw new Error("no spec files");

let count = 0;
for (const file of files) {
	const tasks = parseSpecs(fs.readFileSync(path.join(SPEC_DIR, file), "utf8"));
	for (const t of tasks) {
		for (const key of ["section", "dir", "num", "title", "topics", "input", "desc", "examples", "theory", "tests", "cases", "main", "solution", "commented"]) {
			if (t[key] === undefined || t[key] === "") {
				throw new Error(file + ": " + (t.dir || t.title) + " missing " + key);
			}
		}
		t.run = "run_tests" + t.num;
		const dir = path.join(OUT_DIR, t.section, t.dir);

		write(path.join(dir, "README.md"), readme(t));
		write(path.join(dir, "theory.md"), theory(t));
		write(path.join(dir, "tests.md"), tests(t));
		write(path.join(dir, "main.go"), t.main);
		write(path.join(dir, "solution.go"), t.solution);
		write(path.join(dir, "solution_commented.go"), t.commented);
		write(path.join(dir, t.run + ".sh"), runner(t));

		count++;
		console.log("wrote " + t.section + "/" + t.dir);
	}
}

console.log("total tasks: " + count);
