import { Component, Input } from '@angular/core'

type ButtonStyle = 'primary' | 'secondary'

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
}
