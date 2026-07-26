package com.example;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import org.junit.jupiter.api.Test;

public class CalculatorTest {
    private final Calculator calculator = new Calculator();

    @Test
    public void testAddition() {
        assertEquals(12, calculator.add(5, 7));
    }

    @Test
    public void testMaxTrueBranch() {
        assertEquals(20, calculator.max(20, 10));
    }

    @Test
    public void testMaxFalseBranch() {
        assertEquals(15, calculator.max(5, 15));
    }

    @Test
    public void testDivision() {
        assertEquals(5, calculator.divide(10, 2));
    }

    @Test
    public void testDivisionByZero() {
        Exception exception = assertThrows(IllegalArgumentException.class, () -> calculator.divide(10, 0));
        assertEquals("Division by zero", exception.getMessage());
    }
}
