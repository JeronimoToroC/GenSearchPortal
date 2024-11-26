import { Component, Input } from '@angular/core'

type ButtonStyle = 'primary' | 'secondary'

@Component({
    selector: 'app-button',
    standalone: true,
    templateUrl: './button.component.html',
    styleUrl: './button.component.scss',
})
export class ButtonComponent {
    @Input() title: string = ''
    @Input() style: ButtonStyle = 'primary'
}
