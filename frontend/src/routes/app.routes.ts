import { Routes } from '@angular/router'
import { LoginComponent } from '@screens/login/login.component'
import { HomeComponent } from '@screens/home/home.component'
import { RegisterComponent } from '@screens/register/register.component' // Importar el componente de registro
import { authGuard, authRedirectGuard } from '@guards/auth.guard'

export const routes: Routes = [
    {
        path: '',
        redirectTo: 'login',
        pathMatch: 'full',
    },
    {
        path: 'login',
        component: LoginComponent,
        canActivate: [authRedirectGuard],
    },
    {
        path: 'register',
        component: RegisterComponent,
        canActivate: [authRedirectGuard],
    },
    {
        path: 'home',
        component: HomeComponent,
        canActivate: [authGuard],
    },
    {
        path: '**',
        redirectTo: 'login',
    },
]
