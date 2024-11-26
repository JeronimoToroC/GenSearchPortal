import { Component } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { ButtonComponent } from '@common-components/Button/button.component'
import { LinkToCreateAccountComponent } from '@specific-components/login/link-to-create-account/link-to-create-account.component'

@Component({
    selector: 'app-login',
    standalone: true,
    imports: [FormsModule, ButtonComponent, LinkToCreateAccountComponent],
    templateUrl: './login.component.html',
    styleUrl: './login.component.scss',
})
export class LoginComponent {
    email: string = ''
    password: string = ''

    onSubmit(): void {
        console.log('Login:', { email: this.email, password: this.password })
    }
}
