import { Component, inject } from '@angular/core'
import { Router } from '@angular/router'
import { ToastrService } from 'ngx-toastr'
import { UserGlobalState } from '@globalStates/user.globalstate'

@Component({
    selector: 'app-logout-button',
    standalone: true,
    templateUrl: './logout-button.component.html',
    styleUrls: ['./logout-button.component.scss'],
})
export class LogoutButtonComponent {
    private readonly router = inject(Router)
    private readonly toastr = inject(ToastrService)
    private readonly userGlobalState = inject(UserGlobalState)

    logout(): void {
        this.userGlobalState.setUser(null) // Limpia el estado global
        this.toastr.success('Sesión cerrada exitosamente')
        this.router.navigate(['/login']) // Redirige al login
    }
}
