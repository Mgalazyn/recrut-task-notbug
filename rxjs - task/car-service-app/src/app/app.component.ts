import { Component } from '@angular/core';
import { Car } from './car';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'car-service-app';

  getData()
  {
    const data: Car = {
      name:'VW GOLF',
      model: '5',
      year: 2004,
      parts: 'left doors',
      cost: 100,
    }
    return data;
  }
}
