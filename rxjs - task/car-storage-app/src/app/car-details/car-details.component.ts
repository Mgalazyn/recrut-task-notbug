import { Component } from '@angular/core';

interface Service {
  part: string;
  cost: number;
}

interface Car {
  make: string;
  model: string;
  year: number;
  services: Service[];
}

@Component({
  selector: 'app-car-details',
  templateUrl: './car-details.component.html',
  styleUrls: ['./car-details.component.css']
})
export class CarDetailsComponent {
  car: Car = { make: '', model: '', year: 0, services: [] };
  newService: Service = { part: '', cost: 0 };

  constructor() {
    const carData = localStorage.getItem('car');
    if (carData) {
      this.car = JSON.parse(carData);
    }
  }

  saveCar() {
    localStorage.setItem('car', JSON.stringify(this.car));
  }

  addService() {
    this.car.services.push(this.newService);
    this.newService = { part: '', cost: 0 };
  }
}
