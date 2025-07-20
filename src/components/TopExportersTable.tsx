import { Building, TrendingUp, ExternalLink } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";

interface ExporterData {
  rank: number;
  company: string;
  country: string;
  volume: string;
  marketShare: number;
  growth: string;
  products: string[];
}

export const TopExportersTable = () => {
  const exporters: ExporterData[] = [
    {
      rank: 1,
      company: "Teva Pharmaceutical",
      country: "Israel",
      volume: "$72.4B",
      marketShare: 8.5,
      growth: "+15.2%",
      products: ["Generic APIs", "Biosimilars", "OTC"]
    },
    {
      rank: 2,
      company: "Novartis",
      country: "Switzerland",
      volume: "$65.8B",
      marketShare: 7.8,
      growth: "+12.7%",
      products: ["Oncology", "Cardiovascular", "CNS"]
    },
    {
      rank: 3,
      company: "Pfizer",
      country: "United States",
      volume: "$58.9B",
      marketShare: 7.0,
      growth: "+9.8%",
      products: ["Vaccines", "Oncology", "Immunology"]
    },
    {
      rank: 4,
      company: "Roche",
      country: "Switzerland",
      volume: "$54.2B",
      marketShare: 6.4,
      growth: "+18.3%",
      products: ["Diagnostics", "Oncology", "Immunology"]
    },
    {
      rank: 5,
      company: "Johnson & Johnson",
      country: "United States",
      volume: "$47.6B",
      marketShare: 5.6,
      growth: "+6.9%",
      products: ["Consumer Health", "Pharmaceuticals", "Medical Devices"]
    }
  ];

  return (
    <Card className="bg-gradient-card shadow-card border-border">
      <CardHeader>
        <CardTitle className="text-lg flex items-center gap-2">
          <Building className="w-5 h-5" />
          Top Global Exporters
        </CardTitle>
      </CardHeader>
      <CardContent>
        <div className="space-y-4">
          {exporters.map((exporter) => (
            <div key={exporter.rank} className="flex items-center justify-between p-4 bg-background/50 rounded-lg border border-border hover:bg-background/70 transition-colors">
              <div className="flex items-center gap-4">
                <div className="w-8 h-8 bg-gradient-primary rounded-lg flex items-center justify-center text-primary-foreground font-bold">
                  {exporter.rank}
                </div>
                
                <div className="space-y-1">
                  <div className="flex items-center gap-2">
                    <h3 className="font-semibold text-foreground">{exporter.company}</h3>
                    <span className="text-sm text-muted-foreground">• {exporter.country}</span>
                  </div>
                  
                  <div className="flex items-center gap-2">
                    {exporter.products.slice(0, 2).map((product, idx) => (
                      <Badge key={idx} variant="secondary" className="text-xs">
                        {product}
                      </Badge>
                    ))}
                    {exporter.products.length > 2 && (
                      <span className="text-xs text-muted-foreground">+{exporter.products.length - 2} more</span>
                    )}
                  </div>
                </div>
              </div>

              <div className="flex items-center gap-6">
                <div className="text-right">
                  <div className="text-lg font-bold text-foreground">{exporter.volume}</div>
                  <div className="text-xs text-muted-foreground">{exporter.marketShare}% market share</div>
                </div>
                
                <div className="text-right">
                  <div className="flex items-center gap-1 text-success text-sm font-medium">
                    <TrendingUp className="w-3 h-3" />
                    {exporter.growth}
                  </div>
                  <div className="text-xs text-muted-foreground">YoY growth</div>
                </div>

                <Button variant="outline" size="sm">
                  <ExternalLink className="w-4 h-4" />
                </Button>
              </div>
            </div>
          ))}
        </div>

        <div className="mt-6 text-center">
          <Button variant="outline" className="w-full">
            View All Exporters
          </Button>
        </div>
      </CardContent>
    </Card>
  );
};