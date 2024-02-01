import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { UsecaseRoutingModule } from './usecase-routing.module';
import { NgxSpinnerModule } from 'ngx-spinner';


@NgModule({
  declarations: [
  ],
  imports: [
    CommonModule,
    UsecaseRoutingModule,
    NgxSpinnerModule
  ]
})
export class UsecaseModule { }
