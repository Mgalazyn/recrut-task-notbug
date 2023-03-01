import { Component } from '@angular/core';
import { take } from 'rxjs';
import { DataService } from '../data.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  myData: any;
  myData$: any;
  constructor(private DataService: DataService) {}

  ngOnInit(): void {
    this.myData$ = this.DataService.getData().pipe(take(1)).subscribe((data) => {
      this.myData = data;
    });
  }
  
}
