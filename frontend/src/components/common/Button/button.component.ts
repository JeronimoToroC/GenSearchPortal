import { Component, Input } from '@angular/core'

type ButtonStyle = 'primary' | 'secondary' | 'gray' | 'primary-dark'

@Component({
    selector: 'app-button',
    standalone: true,
    templateUrl: './button.component.html',
    styleUrls: ['./button.component.scss'],
})
export class ButtonComponent {
    @Input() title: string = ''
    @Input() style: ButtonStyle = 'primary'
    @Input() type: 'button' | 'submit' = 'button'
    @Input() disabled: boolean = false
    @Input() height: string = 'auto'
    @Input() width: string = 'auto'
    @Input() fontSize: string = '14px'
}
