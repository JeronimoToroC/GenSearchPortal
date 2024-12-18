import { LinkToCreateAccountComponent } from '@specific-components/login/link-to-create-account/link-to-create-account.component'
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms'
import { FormErrorComponent } from '@common-components/FormError/form-error.component'
import { ButtonComponent } from '@common-components/Button/button.component'
import { RequestService } from '@services/request/request.service'
import { UserGlobalState } from '@globalStates/user.globalstate'
import { Component, inject } from '@angular/core'
import { UserLoginDto } from '@dtos/user.dtos'
import { UserModel } from '@models/user.model'
import { ToastrService } from 'ngx-toastr'
import { Router } from '@angular/router'

@Component({
    selector: 'app-login',
    standalone: true,
    imports: [ReactiveFormsModule, ButtonComponent, LinkToCreateAccountComponent, FormErrorComponent],
    templateUrl: './login.component.html',
    styleUrl: './login.component.scss',
})
export class LoginComponent {
    private readonly fb = inject(FormBuilder)
    private readonly router = inject(Router)
    private readonly toastr = inject(ToastrService)
    private readonly requestService = inject(RequestService)
    private readonly userGlobalState = inject(UserGlobalState)

    loginForm: FormGroup = this.fb.group({
        email: ['', [Validators.required, Validators.email]],
        password: ['', [Validators.required, Validators.minLength(6)]],
    })

    async onSubmit(): Promise<void> {
        if (this.loginForm.invalid) {
            return
        }

        try {
            const loginDto: UserLoginDto = this.loginForm.value
            const response = await this.requestService.post<UserModel>('/login', loginDto)

            if (response) {
                this.userGlobalState.setUser(response)
                await this.router.navigate(['/home'])
                this.toastr.success('Sesión iniciada correctamente')
            }
        } catch (error: any) {
            console.error('Error en el proceso de login:', error)

            if (error.response?.status === 401) {
                this.toastr.error('Credenciales inválidas')
            } else {
                this.toastr.error('Error al iniciar sesión. Intenta nuevamente.')
            }
        }
    }
}
