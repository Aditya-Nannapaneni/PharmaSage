import { Bell, Search, Settings, Globe } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

export const DashboardHeader = () => {
  return (
    <header className="border-b border-border bg-gradient-card shadow-card">
      <div className="flex h-16 items-center justify-between px-6">
        <div className="flex items-center gap-6">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 bg-gradient-primary rounded-lg flex items-center justify-center">
              <Globe className="w-5 h-5 text-primary-foreground" />
            </div>
            <h1 className="text-xl font-bold text-foreground">PharmaSage InsightGrid</h1>
          </div>
          
          <div className="relative">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-muted-foreground" />
            <Input 
              placeholder="Search markets, companies, products..." 
              className="pl-10 w-96 bg-background/50 border-border"
            />
          </div>
        </div>

        <div className="flex items-center gap-3">
          <Button variant="outline" size="sm" className="gap-2">
            <Bell className="w-4 h-4" />
            Alerts
          </Button>
          <Button variant="outline" size="sm" className="gap-2">
            <Settings className="w-4 h-4" />
            Settings
          </Button>
        </div>
      </div>
    </header>
  );
};