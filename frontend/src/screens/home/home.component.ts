import { Component } from '@angular/core'
import { LogoutButtonComponent } from '@common-components/LogoutButton/logout-button.component'

@Component({
    selector: 'app-home',
    standalone: true,
    imports: [LogoutButtonComponent], // Importamos el botón de logout
    templateUrl: './home.component.html',
    styleUrls: ['./home.component.scss'],
})
export class HomeComponent {}
