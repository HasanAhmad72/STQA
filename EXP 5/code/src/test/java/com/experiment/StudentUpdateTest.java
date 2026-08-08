package com.experiment;

import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class StudentUpdateTest {

    private static final String FILE_PATH = "src/test/resources/Students.xlsx";

    @BeforeAll
    public static void createInitialExcelFile() throws IOException {
        Workbook workbook = new XSSFWorkbook();
        Sheet sheet = workbook.createSheet("Students");

        Row header = sheet.createRow(0);
        header.createCell(0).setCellValue("Roll No");
        header.createCell(1).setCellValue("Name");
        header.createCell(2).setCellValue("Marks");
        header.createCell(3).setCellValue("Grade");

        for (int i = 1; i <= 10; i++) {
            Row row = sheet.createRow(i);
            row.createCell(0).setCellValue(100 + i);
            row.createCell(1).setCellValue("Student_" + i);
            row.createCell(2).setCellValue(50.0);
            row.createCell(3).setCellValue("C");
        }

        try (FileOutputStream fos = new FileOutputStream(FILE_PATH)) {
            workbook.write(fos);
        }
        workbook.close();
    }

    @Test
    public void testUpdateTenStudentRecords() throws IOException {
        boolean updateSuccess = StudentRecordUpdater.updateStudentRecords(FILE_PATH);
        assertTrue(updateSuccess, "File update operation failed");

        try (FileInputStream fis = new FileInputStream(FILE_PATH);
             Workbook workbook = new XSSFWorkbook(fis)) {

            Sheet sheet = workbook.getSheetAt(0);

            for (int i = 1; i <= 10; i++) {
                Row row = sheet.getRow(i);
                assertNotNull(row, "Row " + i + " should exist");

                double actualMarks = row.getCell(2).getNumericCellValue();
                String actualGrade = row.getCell(3).getStringCellValue();

                double expectedMarks = 75.0 + i;
                String expectedGrade = expectedMarks >= 80.0 ? "A" : "B";

                assertEquals(expectedMarks, actualMarks, "Marks mismatch for record " + i);
                assertEquals(expectedGrade, actualGrade, "Grade mismatch for record " + i);
            }
        }
    }
}
