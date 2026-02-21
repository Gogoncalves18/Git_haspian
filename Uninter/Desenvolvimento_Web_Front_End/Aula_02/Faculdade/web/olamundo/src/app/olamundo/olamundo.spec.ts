import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Olamundo } from './olamundo';

describe('Olamundo', () => {
  let component: Olamundo;
  let fixture: ComponentFixture<Olamundo>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Olamundo]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Olamundo);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
