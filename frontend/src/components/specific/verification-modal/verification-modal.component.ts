import { Component, Input, Output, EventEmitter } from '@angular/core'
import { CommonModule } from '@angular/common'
import { FormsModule } from '@angular/forms'

@Component({
    selector: 'app-verification-modal',
    standalone: true,
    imports: [CommonModule, FormsModule],
    templateUrl: './verification-modal.component.html',
    styleUrls: ['./verification-modal.component.scss'],
})
export class VerificationModalComponent {
    @Input() isVisible: boolean = false
    @Input() email: string = ''
    @Output() close = new EventEmitter<void>()
    @Output() verify = new EventEmitter<string>()

    verificationCode: string = ''

    closeModal() {
        this.isVisible = false
        this.close.emit()
    }

    verifyCode() {
        this.verify.emit(this.verificationCode)
    }
}
