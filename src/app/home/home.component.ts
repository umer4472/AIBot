import { AfterViewInit, Component, Inject, OnInit, PLATFORM_ID } from '@angular/core';
import { isPlatformBrowser } from '@angular/common';
import Swiper from 'swiper';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements AfterViewInit {
  private swiper: Swiper;

  constructor(@Inject(PLATFORM_ID) private platformId: Object , private router : Router) {}

  getStarted() {
    this.router.navigate(['/Usecase']); // Correct navigation syntax
  }

  ngAfterViewInit() {
    if (isPlatformBrowser(this.platformId)) {
      // Code that interacts with the DOM
      this.initializeSwiper();
    }
  }

  private initializeSwiper() {
    this.swiper = new Swiper('.swiper', {
      slidesPerView: 4,
      spaceBetween: 10,
      loop: false,
      autoplay:{
        delay: 5000,
      }
    });
  }
  onAbout(){
    this.router.navigate(['/about']);
  }
}
