import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ButtonComponent } from '@common-components/Button/button.component';

@Component({
    selector: 'app-login',
    standalone: true,
    imports: [FormsModule, ButtonComponent],
    templateUrl: './login.component.html',
    styleUrl: './login.component.scss'
})
export class LoginComponent {
    email: string = '';
    password: string = '';

    onSubmit(): void {
        // TODO: Implementar lógica de login
        console.log('Login:', { email: this.email, password: this.password });
    }

    onSignUp(): void {
        // TODO: Implementar redirección a registro
        console.log('Redirigiendo a registro...');
    }
}
