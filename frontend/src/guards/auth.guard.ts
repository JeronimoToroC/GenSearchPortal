import { inject } from '@angular/core'
import { Router } from '@angular/router'
import { UserGlobalState } from '@globalStates/user.globalstate'

export const authGuard = () => {
    const router = inject(Router)
    const userGlobalState = inject(UserGlobalState)

    if (userGlobalState.currentUser) {
        return true
    }

    return router.navigate(['/login'])
}

export const authRedirectGuard = async () => {
    const userGlobalState = inject(UserGlobalState)
    const router = inject(Router)

    if (userGlobalState.currentUser) {
        await router.navigate(['/home'])
        return false
    }

    return true
}