import { ButtonComponent } from '@common-components/Button/button.component'
import { CommonModule } from '@angular/common'
import { GenModel } from '@models/gen.model'
import { Component } from '@angular/core'

@Component({
    selector: 'app-home',
    standalone: true,
    imports: [ButtonComponent, CommonModule],
    templateUrl: './home.component.html',
    styleUrl: './home.component.scss',
})
export class HomeComponent {
    genes: GenModel[] = []
    currentPage = 1
    itemsPerPage = 6

    constructor() {
        this.genes = this.generateMockData()
    }

    private generateMockData(): GenModel[] {
        return Array.from({ length: 20 }, (_, i) => ({
            Chrom: `Chr${i + 1}`,
            Pos: `${1000 + i * 100}`,
            Id: `RS${10000 + i}`,
            Ref: ['A', 'T', 'C', 'G'][Math.floor(Math.random() * 4)],
            Alt: ['A', 'T', 'C', 'G'][Math.floor(Math.random() * 4)],
            Qual: (Math.random() * 100).toFixed(2),
            Filter: ['PASS', 'LOW_QUAL'][Math.floor(Math.random() * 2)],
            Info: `Sample info ${i + 1}`,
            Format: 'GT:AD:DP:GQ:PL',
            Output1: `1/1:0,30:30:90:1350,90,0`,
            Output2: `0/1:15,15:30:90:500,0,500`,
        }))
    }

    get totalPages(): number {
        return Math.ceil(this.genes.length / this.itemsPerPage)
    }

    get paginatedGenes(): GenModel[] {
        const startIndex = (this.currentPage - 1) * this.itemsPerPage
        return this.genes.slice(startIndex, startIndex + this.itemsPerPage)
    }

    onPageChange(page: number): void {
        this.currentPage = page
    }
}
