import { TrendingUp, TrendingDown, DollarSign, Package, Users, Globe } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

interface MetricCardProps {
  title: string;
  value: string;
  change: string;
  trend: 'up' | 'down';
  icon: React.ReactNode;
}

const MetricCard = ({ title, value, change, trend, icon }: MetricCardProps) => {
  return (
    <Card className="bg-gradient-card shadow-card border-border hover:shadow-glow transition-all duration-300">
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
        <CardTitle className="text-sm font-medium text-muted-foreground">{title}</CardTitle>
        <div className="w-4 h-4 text-muted-foreground">{icon}</div>
      </CardHeader>
      <CardContent>
        <div className="text-2xl font-bold text-foreground">{value}</div>
        <div className={`text-xs flex items-center gap-1 ${trend === 'up' ? 'text-success' : 'text-destructive'}`}>
          {trend === 'up' ? <TrendingUp className="w-3 h-3" /> : <TrendingDown className="w-3 h-3" />}
          {change}
        </div>
      </CardContent>
    </Card>
  );
};

export const MetricsGrid = () => {
  const metrics = [
    {
      title: "Global Trade Volume",
      value: "$847.2B",
      change: "+12.3% from last year",
      trend: 'up' as const,
      icon: <DollarSign className="w-4 h-4" />
    },
    {
      title: "Active Products",
      value: "24,567",
      change: "+847 this month",
      trend: 'up' as const,
      icon: <Package className="w-4 h-4" />
    },
    {
      title: "Export Companies",
      value: "8,941",
      change: "+156 new entrants",
      trend: 'up' as const,
      icon: <Users className="w-4 h-4" />
    },
    {
      title: "Active Markets",
      value: "187",
      change: "-2 regulatory changes",
      trend: 'down' as const,
      icon: <Globe className="w-4 h-4" />
    }
  ];

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      {metrics.map((metric, index) => (
        <MetricCard key={index} {...metric} />
      ))}
    </div>
  );
};