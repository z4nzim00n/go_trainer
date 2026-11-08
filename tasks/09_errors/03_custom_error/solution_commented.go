package main

import (
	"errors"
	"fmt"
)

// ValidationError — своя ошибка: достаточно метода Error() string.
type ValidationError struct {
	Field string
}

func (e *ValidationError) Error() string {
	return "validation failed: " + e.Field
}

func ValidateAge(age int) error {
	if age < 0 {
		return &ValidationError{Field: "age"}
	}
	return nil
}

func main() {
	var age int
	fmt.Scan(&age)
	err := ValidateAge(age)
	if err != nil {
		// errors.As достаёт конкретный тип из ошибки.
		var ve *ValidationError
		if errors.As(err, &ve) {
			fmt.Println("Validation error:", ve.Field)
		}
	} else {
		fmt.Printf("Age: %d\n", age)
	}
}
