import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit() {
  }

  onAbout(){
    this.router.navigate(['/about']);
  }
  onHome(){
    this.router.navigate(['']);
  }
  onContact(){
    this.router.navigate(['/ContactUs']);
  }
  OnGrammerchecker(){
    this.router.navigate(['/GrammerChecker']);
  }
  Onplagiarismchecker(){
    this.router.navigate(['/PlagiarismChecker']);
  }
  OnchatBot(){
    this.router.navigate(['/ChatBot']);
  }

}
