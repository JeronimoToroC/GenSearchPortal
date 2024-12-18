export interface GenModel {
    Chrom: string;
    Pos: string;
    Id: string;
    Ref: string;
    Alt: string;
    Qual: string;
    Filter: string;
    Info: string;
    Format: string;
    [key: string]: string;
}
