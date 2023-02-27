import { TestBed } from '@angular/core/testing';

interface CarService {
  part: string;
  cost: number;
}

describe('CarService', () => {
  let service: CarService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
