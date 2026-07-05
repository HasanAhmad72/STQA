package com.example;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import org.junit.jupiter.api.Test;

public class AppTest {

    App app = new App();

    @Test
    public void testAddition() {
        assertEquals(12,
                app.add(5, 7));
    }

    @Test
    public void testMaxTrueBranch() {
        assertEquals(20,
                app.max(20, 10));
    }

    @Test
    public void testMaxFalseBranch() {
        assertEquals(15,
                app.max(5, 15));
    }

    @Test
    public void testDivision() {
        assertEquals(5,
                app.divide(10, 2));
    }

    @Test
    public void testDivisionByZero() {
        Exception exception
                = assertThrows(
                        IllegalArgumentException.class,
                        () -> app.divide(10, 0));
        assertEquals(
                "Division by zero",
                exception.getMessage());
    }
}
