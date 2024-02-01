import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PlagiarismCheckerService {
  private apiUrl = 'https://plagiarism-checker-and-auto-citation-generator-multi-lingual.p.rapidapi.com/plagiarism';
  private rapidApiKey = 'd673b331acmsh29fca2d1fa03c58p18a7aejsn8822f575c2c0';
  private rapidApiHost = 'plagiarism-checker-and-auto-citation-generator-multi-lingual.p.rapidapi.com';

  constructor(private http: HttpClient) { }

  checkPlagiarism(text: string, language: string, includeCitations: boolean, scrapeSources: boolean): Observable<any> {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'X-RapidAPI-Key': this.rapidApiKey,
      'X-RapidAPI-Host': this.rapidApiHost
    });
    const options = { headers: headers };
    const body = {
      text: text,
      language: language,
      includeCitations: includeCitations,
      scrapeSources: scrapeSources
    };
    return this.http.post(this.apiUrl, body, options);
  }
}
