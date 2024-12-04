import { ButtonComponent } from '@common-components/Button/button.component'
import { Component } from '@angular/core'

@Component({
    selector: 'app-home',
    standalone: true,
    imports: [ButtonComponent],
    templateUrl: './home.component.html',
    styleUrl: './home.component.scss',
})
export class HomeComponent {}
