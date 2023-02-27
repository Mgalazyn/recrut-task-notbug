import { Injectable } from '@angular/core';
import { Car } from './car';

@Injectable({
  providedIn: 'root'
})
export class CarsService {
  private readonly CARS_STORAGE_KEY = 'cars';

  getCars(): Car[] {
    const carsJson = localStorage.getItem(this.CARS_STORAGE_KEY);
    return carsJson ? JSON.parse(carsJson) : [];
  }

  saveCar(car: Car) {
    const cars = this.getCars();
    const existingCarIndex = cars.findIndex(c => c.name === car.name && c.model === car.model && c.year === car.year && c.parts === car.parts 
      && c.cost === car.cost);
    if (existingCarIndex === -1) {
      cars.push(car);
    } else {
      cars[existingCarIndex] = car;
    }
    localStorage.setItem(this.CARS_STORAGE_KEY, JSON.stringify(cars));
  }
}
