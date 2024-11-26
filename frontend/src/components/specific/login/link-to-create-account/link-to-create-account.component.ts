import { Component } from '@angular/core'

@Component({
    selector: 'app-link-to-create-account',
    standalone: true,
    templateUrl: './link-to-create-account.component.html',
    styleUrl: './link-to-create-account.component.scss',
})
export class LinkToCreateAccountComponent {
    onSignUp(): void {
        // TODO: Implementar redirección a registro
        console.log('Redirigiendo a registro...')
    }
}
