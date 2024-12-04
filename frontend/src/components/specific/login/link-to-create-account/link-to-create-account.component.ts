import { Component } from '@angular/core'
import { Router } from '@angular/router'

@Component({
    selector: 'app-link-to-create-account',
    standalone: true,
    templateUrl: './link-to-create-account.component.html',
    styleUrls: ['./link-to-create-account.component.scss'],
})
export class LinkToCreateAccountComponent {
    constructor(private readonly router: Router) {}

    onSignUp(): void {
        this.router.navigate(['/register'])
    }
}
