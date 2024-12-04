import { Component } from '@angular/core'
import { Router } from '@angular/router'

@Component({
    selector: 'app-link-to-login',
    standalone: true,
    templateUrl: './link-to-login.component.html',
    styleUrls: ['./link-to-login.component.scss'],
})
export class LinkToLoginComponent {
    constructor(private readonly router: Router) {}

    onLogin(): void {
        this.router.navigate(['/login']) // Redirigir a la página de login
    }
}
