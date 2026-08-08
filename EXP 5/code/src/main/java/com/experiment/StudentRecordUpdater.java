package com.experiment;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class StudentRecordUpdater {

    public static boolean updateStudentRecords(String filePath) {
        try (FileInputStream fis = new FileInputStream(filePath);
             Workbook workbook = new XSSFWorkbook(fis)) {

            Sheet sheet = workbook.getSheetAt(0);

            for (int i = 1; i <= 10; i++) {
                Row row = sheet.getRow(i);
                if (row == null) {
                    row = sheet.createRow(i);
                }

                Cell marksCell = row.getCell(2);
                if (marksCell == null) {
                    marksCell = row.createCell(2);
                }
                double updatedMarks = 75.0 + i;
                marksCell.setCellValue(updatedMarks);

                Cell gradeCell = row.getCell(3);
                if (gradeCell == null) {
                    gradeCell = row.createCell(3);
                }
                gradeCell.setCellValue(updatedMarks >= 80.0 ? "A" : "B");
            }

            try (FileOutputStream fos = new FileOutputStream(filePath)) {
                workbook.write(fos);
            }
            return true;

        } catch (IOException e) {
            System.err.println("Error updating Excel file: " + e.getMessage());
            return false;
        }
    }
}
