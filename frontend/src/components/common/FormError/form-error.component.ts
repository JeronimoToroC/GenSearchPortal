import { Component, Input } from '@angular/core'
import { AbstractControl } from '@angular/forms'
import { NgIf } from '@angular/common'

@Component({
    selector: 'app-form-error',
    standalone: true,
    imports: [NgIf],
    templateUrl: './form-error.component.html',
    styleUrl: './form-error.component.scss'
})
export class FormErrorComponent {
    @Input() control: AbstractControl | null = null

    private readonly errorMessages: { [key: string]: string } = {
        required: 'Este campo es requerido',
        email: 'El correo electrónico no es válido',
        minlength: 'La longitud mínima no es válida',
        maxlength: 'La longitud máxima no es válida',
        pattern: 'El formato no es válido',
        min: 'El valor mínimo no es válido',
        max: 'El valor máximo no es válido'
    }

    getErrorMessage(): string {
        if (!this.control || !this.control.errors || !this.control.touched) {
            return ''
        }

        const firstError = Object.keys(this.control.errors)[0]
        return this.errorMessages[firstError] || 'Error de validación'
    }
} 