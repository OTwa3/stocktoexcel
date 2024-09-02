package com.stocktoexcel.stocktoexcel.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import java.io.BufferedReader;
import java.io.InputStreamReader;
// import org.springframework.web.bind.annotation.PostMapping;
// import org.springframework.web.bind.annotation.RequestBody;



@Controller
@RequestMapping("/script")
public class ScriptController {
    @GetMapping("/getScript")
    public String getScript(@RequestParam("ticker") String ticker, @RequestParam("startdate") String startdate, @RequestParam("enddate") String enddate, @RequestParam("filename") String filename) {
        try {
            
            ProcessBuilder pb = new ProcessBuilder("python", "script.py", ticker, filename, startdate, enddate);
            Process process = pb.start();

           
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
            
            int exitCode = process.waitFor();
                if (exitCode == 1) {
                return "/error";
            }
           
            System.out.println("Script executed successfully");
            return "/success";
        } catch (Exception e) {
            e.printStackTrace();
            return "/error";
        }
        
    }


}

