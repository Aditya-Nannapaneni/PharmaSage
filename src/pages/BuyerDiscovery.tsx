import { Search, Filter, MapPin, Building2, TrendingUp, Users, Download, Eye } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";

const mockBuyers = [
  {
    id: 1,
    name: "MedCore Pharmaceuticals",
    location: "Berlin, Germany",
    segment: "Generic Medications",
    revenue: "$2.4B",
    employees: "5,000-10,000",
    purchasingVolume: "$180M",
    opportunityScore: 92,
    status: "Hot Lead",
    lastContact: "2 days ago",
    keyProducts: ["Antibiotics", "Pain Relief", "Cardiovascular"]
  },
  {
    id: 2,
    name: "BioPharma Solutions",
    location: "São Paulo, Brazil",
    segment: "Specialty Drugs",
    revenue: "$890M",
    employees: "1,000-5,000",
    purchasingVolume: "$65M",
    opportunityScore: 78,
    status: "Qualified",
    lastContact: "1 week ago",
    keyProducts: ["Oncology", "Immunology", "Rare Diseases"]
  },
  {
    id: 3,
    name: "Global Health Networks",
    location: "Mumbai, India",
    segment: "Distribution",
    revenue: "$1.2B",
    employees: "2,000-5,000",
    purchasingVolume: "$95M",
    opportunityScore: 85,
    status: "Research",
    lastContact: "3 days ago",
    keyProducts: ["Vaccines", "Generic Drugs", "Medical Devices"]
  },
  {
    id: 4,
    name: "PharmaVision Corp",
    location: "Toronto, Canada",
    segment: "Research & Development",
    revenue: "$450M",
    employees: "500-1,000",
    purchasingVolume: "$28M",
    opportunityScore: 71,
    status: "New Lead",
    lastContact: "5 days ago",
    keyProducts: ["Clinical Trials", "Drug Development", "Biomarkers"]
  }
];

const BuyerDiscovery = () => {
  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b border-border bg-gradient-card shadow-card">
        <div className="flex h-16 items-center justify-between px-6">
          <div className="flex items-center gap-6">
            <h1 className="text-xl font-bold text-foreground">Buyer Discovery Engine</h1>
            <div className="relative">
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-muted-foreground" />
              <Input 
                placeholder="Search buyers by name, location, segment..." 
                className="pl-10 w-96 bg-background/50 border-border"
              />
            </div>
          </div>
          <div className="flex items-center gap-3">
            <Button variant="outline" size="sm" className="gap-2">
              <Download className="w-4 h-4" />
              Export
            </Button>
            <Button className="gap-2">
              <Filter className="w-4 h-4" />
              Advanced Filters
            </Button>
          </div>
        </div>
      </header>

      <main className="p-6 space-y-6">
        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
          <Card className="bg-gradient-card border-border">
            <CardContent className="p-4">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-gradient-primary rounded-lg flex items-center justify-center">
                  <Building2 className="w-5 h-5 text-primary-foreground" />
                </div>
                <div>
                  <p className="text-sm text-muted-foreground">Total Buyers</p>
                  <p className="text-2xl font-bold text-foreground">2,847</p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-gradient-card border-border">
            <CardContent className="p-4">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-gradient-success rounded-lg flex items-center justify-center">
                  <TrendingUp className="w-5 h-5 text-success-foreground" />
                </div>
                <div>
                  <p className="text-sm text-muted-foreground">Hot Leads</p>
                  <p className="text-2xl font-bold text-foreground">156</p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-gradient-card border-border">
            <CardContent className="p-4">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-primary/20 rounded-lg flex items-center justify-center">
                  <Users className="w-5 h-5 text-primary" />
                </div>
                <div>
                  <p className="text-sm text-muted-foreground">Active Prospects</p>
                  <p className="text-2xl font-bold text-foreground">423</p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-gradient-card border-border">
            <CardContent className="p-4">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-accent/20 rounded-lg flex items-center justify-center">
                  <MapPin className="w-5 h-5 text-accent" />
                </div>
                <div>
                  <p className="text-sm text-muted-foreground">Markets</p>
                  <p className="text-2xl font-bold text-foreground">67</p>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Filters */}
        <Card className="bg-gradient-card border-border">
          <CardHeader>
            <CardTitle className="text-foreground">Search Filters</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
              <div>
                <label className="text-sm font-medium text-foreground mb-2 block">Market Segment</label>
                <Select>
                  <SelectTrigger>
                    <SelectValue placeholder="All Segments" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="generic">Generic Medications</SelectItem>
                    <SelectItem value="specialty">Specialty Drugs</SelectItem>
                    <SelectItem value="distribution">Distribution</SelectItem>
                    <SelectItem value="research">Research & Development</SelectItem>
                  </SelectContent>
                </Select>
              </div>
              <div>
                <label className="text-sm font-medium text-foreground mb-2 block">Company Size</label>
                <Select>
                  <SelectTrigger>
                    <SelectValue placeholder="All Sizes" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="small">1-500 employees</SelectItem>
                    <SelectItem value="medium">500-2,000 employees</SelectItem>
                    <SelectItem value="large">2,000+ employees</SelectItem>
                  </SelectContent>
                </Select>
              </div>
              <div>
                <label className="text-sm font-medium text-foreground mb-2 block">Region</label>
                <Select>
                  <SelectTrigger>
                    <SelectValue placeholder="All Regions" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="na">North America</SelectItem>
                    <SelectItem value="eu">Europe</SelectItem>
                    <SelectItem value="asia">Asia Pacific</SelectItem>
                    <SelectItem value="latam">Latin America</SelectItem>
                  </SelectContent>
                </Select>
              </div>
              <div>
                <label className="text-sm font-medium text-foreground mb-2 block">Opportunity Score</label>
                <Select>
                  <SelectTrigger>
                    <SelectValue placeholder="All Scores" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="high">80-100 (High)</SelectItem>
                    <SelectItem value="medium">60-79 (Medium)</SelectItem>
                    <SelectItem value="low">0-59 (Low)</SelectItem>
                  </SelectContent>
                </Select>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Buyer List */}
        <Card className="bg-gradient-card border-border">
          <CardHeader>
            <CardTitle className="text-foreground">Discovered Buyers</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              {mockBuyers.map((buyer) => (
                <div key={buyer.id} className="border border-border rounded-lg p-4 hover:bg-muted/20 transition-colors">
                  <div className="flex items-start justify-between">
                    <div className="flex-1">
                      <div className="flex items-center gap-3 mb-2">
                        <h3 className="font-semibold text-foreground text-lg">{buyer.name}</h3>
                        <Badge 
                          variant={buyer.status === "Hot Lead" ? "default" : "secondary"}
                          className={buyer.status === "Hot Lead" ? "bg-gradient-primary" : ""}
                        >
                          {buyer.status}
                        </Badge>
                        <div className="flex items-center gap-1">
                          <div className="w-2 h-2 bg-gradient-success rounded-full"></div>
                          <span className="text-sm font-medium text-success">
                            {buyer.opportunityScore}% Match
                          </span>
                        </div>
                      </div>
                      
                      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-3">
                        <div className="flex items-center gap-2">
                          <MapPin className="w-4 h-4 text-muted-foreground" />
                          <span className="text-sm text-muted-foreground">{buyer.location}</span>
                        </div>
                        <div className="flex items-center gap-2">
                          <Building2 className="w-4 h-4 text-muted-foreground" />
                          <span className="text-sm text-muted-foreground">{buyer.segment}</span>
                        </div>
                        <div className="flex items-center gap-2">
                          <Users className="w-4 h-4 text-muted-foreground" />
                          <span className="text-sm text-muted-foreground">{buyer.employees}</span>
                        </div>
                      </div>

                      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-3">
                        <div>
                          <span className="text-sm text-muted-foreground">Annual Revenue: </span>
                          <span className="text-sm font-medium text-foreground">{buyer.revenue}</span>
                        </div>
                        <div>
                          <span className="text-sm text-muted-foreground">Purchasing Volume: </span>
                          <span className="text-sm font-medium text-foreground">{buyer.purchasingVolume}</span>
                        </div>
                      </div>

                      <div className="mb-3">
                        <span className="text-sm text-muted-foreground">Key Products: </span>
                        <div className="flex flex-wrap gap-1 mt-1">
                          {buyer.keyProducts.map((product, index) => (
                            <Badge key={index} variant="outline" className="text-xs">
                              {product}
                            </Badge>
                          ))}
                        </div>
                      </div>

                      <div className="text-xs text-muted-foreground">
                        Last Contact: {buyer.lastContact}
                      </div>
                    </div>

                    <div className="flex flex-col gap-2 ml-4">
                      <Button size="sm" className="gap-2">
                        <Eye className="w-4 h-4" />
                        View Profile
                      </Button>
                      <Button variant="outline" size="sm">
                        Contact
                      </Button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </main>
    </div>
  );
};

export default BuyerDiscovery;