import { DashboardHeader } from "@/components/DashboardHeader";
import { MetricsGrid } from "@/components/MetricsGrid";
import { MarketFilters } from "@/components/MarketFilters";
import { WorldMapPlaceholder } from "@/components/WorldMapPlaceholder";
import { TopExportersTable } from "@/components/TopExportersTable";
import { TrendChart } from "@/components/TrendChart";

const Index = () => {
  return (
    <div className="min-h-screen bg-background">
      <DashboardHeader />
      
      <main className="p-6 space-y-6">
        {/* Market Filters */}
        <MarketFilters />
        
        {/* Key Metrics */}
        <MetricsGrid />
        
        {/* Main Content Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* World Map */}
          <WorldMapPlaceholder />
          
          {/* Trend Chart */}
          <TrendChart />
        </div>
        
        {/* Top Exporters Table */}
        <TopExportersTable />
      </main>
    </div>
  );
};

export default Index;
