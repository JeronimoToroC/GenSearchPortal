import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms'
import { FormErrorComponent } from '@common-components/FormError/form-error.component'
import { ButtonComponent } from '@common-components/Button/button.component'
import { VerificationModalComponent } from '@specific-components/verification-modal/verification-modal.component'
import { RequestService } from '@services/request/request.service'
import { Component, inject } from '@angular/core'
import { ToastrService } from 'ngx-toastr'
import { Router } from '@angular/router'
import { LinkToLoginComponent } from '../../components/specific/register/link-to-login/link-to-login.component'

@Component({
    selector: 'app-register',
    standalone: true,
    imports: [
        ReactiveFormsModule,
        ButtonComponent,
        FormErrorComponent,
        LinkToLoginComponent,
        VerificationModalComponent,
    ],
    templateUrl: './register.component.html',
    styleUrls: ['./register.component.scss'],
})
export class RegisterComponent {
    private readonly fb = inject(FormBuilder)
    private readonly router = inject(Router)
    private readonly toastr = inject(ToastrService)
    private readonly requestService = inject(RequestService)

    registerForm: FormGroup = this.fb.group({
        name: ['', [Validators.required, Validators.minLength(3)]],
        email: ['', [Validators.required, Validators.email]],
        password: ['', [Validators.required, Validators.minLength(6)]],
    })

    isModalVisible: boolean = false
    userEmail: string = ''

    async onSubmit(): Promise<void> {
        if (this.registerForm.invalid) {
            return
        }

        try {
            const registerData = this.registerForm.value
            const response = await this.requestService.post('/register', registerData)

            if (response) {
                this.toastr.success('Código de verificación enviado al correo.')
                this.userEmail = registerData.email
                this.isModalVisible = true
            }
        } catch (error) {
            console.error('Error en el proceso de registro:', error)
            this.toastr.error('Error al crear la cuenta. Por favor, intenta nuevamente.')
        }
    }

    handleCloseModal(): void {
        this.isModalVisible = false
    }

    async handleVerifyCode(code: string): Promise<void> {
        try {
            const response = await this.requestService.post('/verify-otp', {
                email: this.userEmail,
                otp_code: code,
            })

            if (response) {
                this.toastr.success('Cuenta verificada exitosamente.')
                this.isModalVisible = false
                await this.router.navigate(['/login'])
            }
        } catch (error) {
            console.error('Error al verificar el código:', error)
            this.toastr.error('Código de verificación incorrecto. Por favor, inténtalo nuevamente.')
        }
    }
}
