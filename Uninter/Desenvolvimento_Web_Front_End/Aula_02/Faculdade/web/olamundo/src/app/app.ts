import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Olamundo } from './olamundo/olamundo';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, Olamundo],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('olamundo');
}
