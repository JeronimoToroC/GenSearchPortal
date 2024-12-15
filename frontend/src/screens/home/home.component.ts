import { ButtonComponent } from '@common-components/Button/button.component'
import { CommonModule } from '@angular/common'
import { GenModel } from '@models/gen.model'
import { Component, OnInit } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { LogoutButtonComponent } from '@common-components/LogoutButton/logout-button.component'
import { GenomeService } from '@services/request/geome.service'

@Component({
    selector: 'app-home',
    standalone: true,
    imports: [ButtonComponent, CommonModule, FormsModule, LogoutButtonComponent],
    templateUrl: './home.component.html',
    styleUrls: ['./home.component.scss'],
})
export class HomeComponent implements OnInit {
    genes: GenModel[] = []
    currentPage = 1
    itemsPerPage = 6
    isLastPage = false
    searchInput = ''
    noResults = false

    constructor(private readonly genomeService: GenomeService) {}

    ngOnInit(): void {
        this.loadGenomes()
    }

    async loadGenomes(): Promise<void> {
        try {
            const response = await this.genomeService.searchGenomes(
                this.searchInput,
                this.currentPage,
                this.itemsPerPage
            )
            this.genes = response.resultados
            this.noResults = response.resultados.length === 0
            this.isLastPage = response.resultados.length < this.itemsPerPage
        } catch (error) {
            console.error('Error loading genomes:', error)
            this.noResults = true
            this.genes = []
        }
    }

    get paginatedGenes(): GenModel[] {
        return this.genes
    }

    onSearch(): void {
        this.currentPage = 1
        this.isLastPage = false
        this.noResults = false
        this.loadGenomes()
    }

    onPageChange(page: number): void {
        if (page > 0 && !this.isLastPage) {
            this.currentPage = page
            this.loadGenomes()
        }
    }
}
