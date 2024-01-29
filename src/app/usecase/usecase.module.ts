import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { UsecaseRoutingModule } from './usecase-routing.module';
import { HomeComponent } from '../home/home.component';
import { NavbarComponent } from '../navbar/navbar.component';


@NgModule({
  declarations: [
  ],
  imports: [
    CommonModule,
    UsecaseRoutingModule
  ]
})
export class UsecaseModule { }
