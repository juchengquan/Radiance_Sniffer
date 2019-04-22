package main

import "fmt"
import "time"
import "net/http"
import "os"
import "io"
import "log"

func main() {

	urlPath := "http://www.solar-repository.sg/ftp_up/irradiance/NSR_IrrMap.png"

	currentDir := getCurrentDir() // get current dir

	// in the loop
	for i:=0; i<100; i++ {
		resp := getFigureFromURL(urlPath)
		fileName := generateFileName() // get file name

		saveFigureIntoFile(currentDir, fileName, resp)

		time.Sleep(59 * time.Second)
		fmt.Println("save a file at: "+time.Now().Format("20060102_1504"))
	}
	fmt.Println("All Done!")
} 

func generateFileName() string {
	timeNow:= time.Now().Format("20060102_1504")
	return timeNow+".png"
}

func getCurrentDir() string {
	dir, err := os.Getwd() //get current directory
	if err != nil {
		log.Fatal(err)
	}
	return dir
}

func getFigureFromURL(urlPath string) *http.Response {
	resp, err := http.Get(urlPath)
	if err != nil {
		fmt.Println(err)
		log.Fatal(err)
	}
	return resp
}

func saveFigureIntoFile (currentDir string, fileName string, resp *http.Response) {
	os.MkdirAll(".\\figures", os.ModePerm)

	out, err := os.Create(currentDir+"\\figures\\"+fileName)
	if err != nil {
		log.Fatal(err)
	}

	io.Copy(out, resp.Body)
}
