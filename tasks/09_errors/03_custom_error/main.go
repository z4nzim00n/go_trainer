package main

import (
	"errors"
	"fmt"
)

// TODO: объяви ValidationError и ValidateAge

type ValidationError struct {
	Field string
}

func (e *ValidationError) Error() string {
	return "validation failed: " + e.Field
}

func ValidateAge(age int) error {
	return nil
}

func main() {
	var age int
	fmt.Scan(&age)
	err := ValidateAge(age)
	if err != nil {
		var ve *ValidationError
		if errors.As(err, &ve) {
			fmt.Println("Validation error:", ve.Field)
		}
	} else {
		fmt.Printf("Age: %d\n", age)
	}
}
