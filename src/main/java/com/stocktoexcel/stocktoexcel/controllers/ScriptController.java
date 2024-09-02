package com.stocktoexcel.stocktoexcel.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import java.io.BufferedReader;
import java.io.InputStreamReader;


@Controller
@RequestMapping("/script")
public class ScriptController {
    @GetMapping("/getScript")
    public String getScript(@RequestParam("ticker") String ticker, @RequestParam("date") String date, @RequestParam("filename") String filename) {
        try {
            
            ProcessBuilder pb = new ProcessBuilder("python", "script.py", ticker, filename, date);
            Process process = pb.start();

            //Capture output (optional)
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
            
            process.waitFor();
        } catch (Exception e) {
            e.printStackTrace();
        }
        System.out.println("Script executed successfully");
        return "/success";
    }
}

