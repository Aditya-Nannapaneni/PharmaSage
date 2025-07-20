import { TrendingUp, BarChart3 } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export const TrendChart = () => {
  // Mock data for the chart visualization
  const chartData = [
    { month: 'Jan', value: 65, color: 'bg-primary' },
    { month: 'Feb', value: 78, color: 'bg-primary' },
    { month: 'Mar', value: 82, color: 'bg-success' },
    { month: 'Apr', value: 74, color: 'bg-primary' },
    { month: 'May', value: 88, color: 'bg-success' },
    { month: 'Jun', value: 95, color: 'bg-success' },
    { month: 'Jul', value: 92, color: 'bg-success' },
    { month: 'Aug', value: 87, color: 'bg-primary' },
    { month: 'Sep', value: 94, color: 'bg-success' },
    { month: 'Oct', value: 98, color: 'bg-success' },
    { month: 'Nov', value: 89, color: 'bg-primary' },
    { month: 'Dec', value: 102, color: 'bg-accent' }
  ];

  const maxValue = Math.max(...chartData.map(d => d.value));

  return (
    <Card className="bg-gradient-card shadow-card border-border">
      <CardHeader>
        <CardTitle className="text-lg flex items-center gap-2">
          <BarChart3 className="w-5 h-5" />
          Market Trends (2024)
        </CardTitle>
      </CardHeader>
      <CardContent>
        <div className="space-y-6">
          {/* Chart visualization */}
          <div className="h-64 flex items-end justify-between gap-2 p-4 bg-background/20 rounded-lg">
            {chartData.map((data, index) => (
              <div key={index} className="flex flex-col items-center gap-2 flex-1">
                <div 
                  className={`w-full ${data.color} rounded-t-sm transition-all duration-500 hover:opacity-80`}
                  style={{ height: `${(data.value / maxValue) * 100}%` }}
                />
                <span className="text-xs text-muted-foreground">{data.month}</span>
              </div>
            ))}
          </div>

          {/* Key insights */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div className="text-center p-3 bg-background/50 rounded-lg border border-border">
              <div className="text-lg font-bold text-success">+23.7%</div>
              <div className="text-xs text-muted-foreground">Annual Growth</div>
            </div>
            <div className="text-center p-3 bg-background/50 rounded-lg border border-border">
              <div className="text-lg font-bold text-primary">$2.4T</div>
              <div className="text-xs text-muted-foreground">Total Volume</div>
            </div>
            <div className="text-center p-3 bg-background/50 rounded-lg border border-border">
              <div className="text-lg font-bold text-accent">187</div>
              <div className="text-xs text-muted-foreground">Active Markets</div>
            </div>
          </div>

          {/* Trend indicators */}
          <div className="flex items-center justify-between text-sm">
            <div className="flex items-center gap-2 text-success">
              <TrendingUp className="w-4 h-4" />
              <span>Strong upward trend in Q4</span>
            </div>
            <div className="text-muted-foreground">
              Last updated: 2 hours ago
            </div>
          </div>
        </div>
      </CardContent>
    </Card>
  );
};