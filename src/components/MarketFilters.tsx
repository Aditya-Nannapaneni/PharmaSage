import { Calendar, Filter, Download } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export const MarketFilters = () => {
  return (
    <Card className="bg-gradient-card shadow-card border-border">
      <CardHeader>
        <CardTitle className="text-lg flex items-center gap-2">
          <Filter className="w-5 h-5" />
          Market Filters
        </CardTitle>
      </CardHeader>
      <CardContent>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="space-y-2">
            <label className="text-sm font-medium text-foreground">Product Type</label>
            <Select>
              <SelectTrigger className="bg-background/50">
                <SelectValue placeholder="All Products" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="api">API</SelectItem>
                <SelectItem value="fdf">FDF</SelectItem>
                <SelectItem value="excipients">Excipients</SelectItem>
                <SelectItem value="all">All Products</SelectItem>
              </SelectContent>
            </Select>
          </div>

          <div className="space-y-2">
            <label className="text-sm font-medium text-foreground">Region</label>
            <Select>
              <SelectTrigger className="bg-background/50">
                <SelectValue placeholder="Global" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="europe">Europe</SelectItem>
                <SelectItem value="asia">Asia Pacific</SelectItem>
                <SelectItem value="americas">Americas</SelectItem>
                <SelectItem value="africa">Africa</SelectItem>
                <SelectItem value="global">Global</SelectItem>
              </SelectContent>
            </Select>
          </div>

          <div className="space-y-2">
            <label className="text-sm font-medium text-foreground">Time Period</label>
            <Select>
              <SelectTrigger className="bg-background/50">
                <SelectValue placeholder="Last 12 months" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="1m">Last Month</SelectItem>
                <SelectItem value="3m">Last 3 Months</SelectItem>
                <SelectItem value="6m">Last 6 Months</SelectItem>
                <SelectItem value="12m">Last 12 Months</SelectItem>
                <SelectItem value="2y">Last 2 Years</SelectItem>
              </SelectContent>
            </Select>
          </div>

          <div className="space-y-2">
            <label className="text-sm font-medium text-foreground">Actions</label>
            <div className="flex gap-2">
              <Button variant="outline" size="sm" className="flex-1">
                <Calendar className="w-4 h-4 mr-2" />
                Custom
              </Button>
              <Button variant="outline" size="sm" className="flex-1">
                <Download className="w-4 h-4 mr-2" />
                Export
              </Button>
            </div>
          </div>
        </div>
      </CardContent>
    </Card>
  );
};