import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core'
import { provideAnimations } from '@angular/platform-browser/animations'
import { provideHttpClient } from '@angular/common/http'
import { provideRouter } from '@angular/router'
import { provideToastr } from 'ngx-toastr'

import { routes } from '@routes/app.routes'

export const appConfig: ApplicationConfig = {
    providers: [
        provideZoneChangeDetection({ eventCoalescing: true }),
        provideRouter(routes),
        provideHttpClient(),
        provideAnimations(),
        provideToastr({
            timeOut: 3000,
            positionClass: 'toast-top-right',
            preventDuplicates: true,
        }),
    ],
}
