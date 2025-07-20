import { MapPin, TrendingUp } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export const WorldMapPlaceholder = () => {
  const regions = [
    { name: "North America", volume: "$127.8B", growth: "+8.2%", color: "bg-primary" },
    { name: "Europe", volume: "$231.4B", growth: "+12.1%", color: "bg-success" },
    { name: "Asia Pacific", volume: "$342.7B", growth: "+15.3%", color: "bg-accent" },
    { name: "Latin America", volume: "$78.9B", growth: "+6.7%", color: "bg-warning" },
    { name: "Africa", volume: "$44.2B", growth: "+18.9%", color: "bg-primary-glow" },
  ];

  return (
    <Card className="bg-gradient-card shadow-card border-border">
      <CardHeader>
        <CardTitle className="text-lg flex items-center gap-2">
          <MapPin className="w-5 h-5" />
          Global Trade Flows
        </CardTitle>
      </CardHeader>
      <CardContent>
        <div className="relative h-80 bg-background/20 rounded-lg border border-border overflow-hidden">
          {/* World Map Placeholder with visual elements */}
          <div className="absolute inset-0 bg-gradient-to-br from-primary/10 via-accent/5 to-success/10" />
          
          <div className="absolute inset-0 flex items-center justify-center">
            <div className="text-center">
              <div className="w-24 h-24 bg-gradient-primary rounded-full mx-auto mb-4 flex items-center justify-center">
                <MapPin className="w-12 h-12 text-primary-foreground" />
              </div>
              <h3 className="text-lg font-semibold text-foreground mb-2">Interactive World Map</h3>
              <p className="text-sm text-muted-foreground">
                Real-time visualization of global pharma trade flows
              </p>
            </div>
          </div>

          {/* Regional indicators */}
          <div className="absolute top-4 left-4 space-y-2">
            {regions.slice(0, 3).map((region, index) => (
              <div key={index} className="flex items-center gap-2 bg-background/80 backdrop-blur-sm rounded-md px-2 py-1">
                <div className={`w-2 h-2 rounded-full ${region.color}`} />
                <span className="text-xs text-foreground">{region.name}</span>
              </div>
            ))}
          </div>

          <div className="absolute top-4 right-4 space-y-2">
            {regions.slice(3).map((region, index) => (
              <div key={index} className="flex items-center gap-2 bg-background/80 backdrop-blur-sm rounded-md px-2 py-1">
                <div className={`w-2 h-2 rounded-full ${region.color}`} />
                <span className="text-xs text-foreground">{region.name}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Regional Summary */}
        <div className="mt-6 grid grid-cols-2 md:grid-cols-5 gap-4">
          {regions.map((region, index) => (
            <div key={index} className="text-center p-3 bg-background/50 rounded-lg border border-border">
              <div className={`w-3 h-3 rounded-full ${region.color} mx-auto mb-2`} />
              <div className="text-xs text-muted-foreground mb-1">{region.name}</div>
              <div className="text-sm font-semibold text-foreground">{region.volume}</div>
              <div className="text-xs text-success flex items-center justify-center gap-1">
                <TrendingUp className="w-3 h-3" />
                {region.growth}
              </div>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  );
};