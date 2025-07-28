import { useState, useEffect } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Separator } from "@/components/ui/separator";
import { Label } from "@/components/ui/label";
import { Search, Filter, Download, Building2, MapPin, Users, TrendingUp, Star, Phone, Mail, Calendar, Globe, Target, BarChart3, ExternalLink, Loader2, CheckCircle, AlertCircle, Play, Eye, MessageCircle } from "lucide-react";

// Helper function to extract company name from URL
const extractCompanyNameFromUrl = (url: string): string => {
  try {
    const hostname = new URL(url).hostname;
    return hostname.replace(/^www\./, '').split('.')[0];
  } catch (e) {
    return url;
  }
};

const BuyerDiscovery = () => {
  const [companyUrl, setCompanyUrl] = useState("");
  const [isResearching, setIsResearching] = useState(false);
  const [hasResults, setHasResults] = useState(false);
  const [activeUIOption, setActiveUIOption] = useState("cards");
  const [selectedBuyer, setSelectedBuyer] = useState<number | null>(null);
  const [researchResults, setResearchResults] = useState<any>(null);
  const [error, setError] = useState<Error | null>(null);
  const [apiMode, setApiMode] = useState<string | null>(null);

  // Check API mode in development
  useEffect(() => {
    if (import.meta.env.DEV) {
      fetch('/api/research/status')
        .then(res => res.json())
        .then(data => {
          setApiMode(data.mode);
        })
        .catch(err => console.error('Failed to check API status:', err));
    }
  }, []);

  const handleResearch = async () => {
    if (!companyUrl) return;
    
    setIsResearching(true);
    setError(null);
    
    try {
      // Extract company name from URL
      const companyName = extractCompanyNameFromUrl(companyUrl);
      
      // Make API call to backend
      const response = await fetch('/api/research/buyers', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          company_name: companyName,
          company_website: companyUrl,
          products: ["Generic APIs"], // Default products, could be made configurable
        }),
      });
      
      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || `Research failed: ${response.statusText}`);
      }
      
      const results = await response.json();
      setResearchResults(results);
      setHasResults(true);
    } catch (err) {
      console.error("Research failed:", err);
      setError(err instanceof Error ? err : new Error(String(err)));
    } finally {
      setIsResearching(false);
    }
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case "High Priority":
        return "bg-gradient-primary";
      case "Medium Priority":
        return "bg-yellow-500";
      case "Low Priority":
        return "bg-gray-500";
      default:
        return "bg-gray-500";
    }
  };

  const getOpportunityScoreColor = (score: number) => {
    if (score >= 90) return "text-green-600";
    if (score >= 80) return "text-yellow-600";
    return "text-gray-600";
  };

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b border-border bg-gradient-card shadow-card">
        <div className="flex h-16 items-center justify-between px-6">
          <div className="flex items-center gap-6">
            <h1 className="text-xl font-bold text-foreground">AI-Powered Buyer Discovery Engine</h1>
          </div>
          <div className="flex items-center gap-3">
            {hasResults && (
              <>
                <Button variant="outline" size="sm" className="gap-2">
                  <Download className="w-4 h-4" />
                  Export Report
                </Button>
                <Button variant="outline" size="sm" className="gap-2">
                  <MessageCircle className="w-4 h-4" />
                  Generate Outreach
                </Button>
              </>
            )}
          </div>
        </div>
      </header>

      <main className="p-6 space-y-6">
        {/* Development Mode Indicator */}
        {import.meta.env.DEV && apiMode && (
          <div className="p-2 bg-yellow-100 text-yellow-800 text-sm rounded-md mb-4">
            <div className="flex items-center gap-2">
              <span>API Mode:</span>
              <span className="font-medium">
                {apiMode === 'mock' ? 'Using Mock Data' : 'Using Live API'}
              </span>
              <span className="text-xs">
                (Controlled by USE_MOCK_RESPONSES environment variable in backend)
              </span>
            </div>
          </div>
        )}

        {/* Research Input Form */}
        <Card className="bg-gradient-card border-border">
          <CardHeader>
            <CardTitle className="flex items-center gap-2 text-foreground">
              <Target className="w-5 h-5" />
              Company Research & Buyer Discovery
            </CardTitle>
            <p className="text-sm text-muted-foreground">
              Enter your company's website URL to discover potential buyers and partners using AI-powered market research.
            </p>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="company-url">Source Company Website URL</Label>
              <div className="flex gap-2">
                <Input
                  id="company-url"
                  placeholder="https://www.yourcompany.com"
                  value={companyUrl}
                  onChange={(e) => setCompanyUrl(e.target.value)}
                  className="flex-1"
                />
                <Button 
                  onClick={handleResearch}
                  disabled={!companyUrl || isResearching}
                  className="gap-2 min-w-[140px]"
                >
                  {isResearching ? (
                    <>
                      <Loader2 className="w-4 h-4 animate-spin" />
                      Researching...
                    </>
                  ) : (
                    <>
                      <Play className="w-4 h-4" />
                      Start Research
                    </>
                  )}
                </Button>
              </div>
            </div>
            
            {isResearching && (
              <div className="bg-muted/20 rounded-lg p-4 space-y-2">
                <div className="flex items-center gap-2">
                  <Loader2 className="w-4 h-4 animate-spin" />
                  <span className="text-sm font-medium">AI Research in Progress...</span>
                </div>
                <div className="text-xs text-muted-foreground space-y-1">
                  <div>• Analyzing company website and business model</div>
                  <div>• Identifying product portfolio and capabilities</div>
                  <div>• Defining ideal customer profile</div>
                  <div>• Searching for real target companies</div>
                  <div>• Generating evidence-backed recommendations</div>
                </div>
              </div>
            )}
            
            {error && (
              <div className="bg-red-50 text-red-800 p-3 rounded-md flex items-start gap-2">
                <AlertCircle className="w-5 h-5 mt-0.5" />
                <div>
                  <p className="font-medium">Research failed</p>
                  <p className="text-sm">{error.message}</p>
                </div>
              </div>
            )}
          </CardContent>
        </Card>

        {/* Results Section */}
        {hasResults && researchResults && (
          <>
            {/* Source Company Overview */}
            <Card className="bg-gradient-card border-border">
              <CardHeader>
                <CardTitle className="flex items-center gap-2 text-foreground">
                  <Building2 className="w-5 h-5" />
                  Source Company Analysis
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <div>
                  <h3 className="font-semibold text-foreground mb-2">{researchResults.sourceCompany.name}</h3>
                  <p className="text-sm text-muted-foreground mb-3">{researchResults.sourceCompany.overview}</p>
                  
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                      <h4 className="font-medium text-foreground mb-1">Business Model</h4>
                      <p className="text-sm text-muted-foreground">{researchResults.sourceCompany.businessModel}</p>
                    </div>
                    <div>
                      <h4 className="font-medium text-foreground mb-1">Therapeutic Coverage</h4>
                      <p className="text-sm text-muted-foreground">{researchResults.sourceCompany.therapeuticCoverage}</p>
                    </div>
                  </div>
                </div>

                <Separator />
                
                <div>
                  <h4 className="font-medium text-foreground mb-2">Ideal Customer Profile</h4>
                  <p className="text-sm text-muted-foreground">{researchResults.idealCustomerProfile}</p>
                </div>
              </CardContent>
            </Card>

            {/* Stats Cards */}
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
              <Card className="bg-gradient-card border-border">
                <CardContent className="p-4">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 bg-gradient-primary rounded-lg flex items-center justify-center">
                      <Target className="w-5 h-5 text-primary-foreground" />
                    </div>
                    <div>
                      <p className="text-sm text-muted-foreground">Targets Found</p>
                      <p className="text-2xl font-bold text-foreground">{researchResults.discoveredBuyers.length}</p>
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
                      <p className="text-sm text-muted-foreground">High Priority</p>
                      <p className="text-2xl font-bold text-foreground">
                        {researchResults.discoveredBuyers.filter(b => b.status === "High Priority").length}
                      </p>
                    </div>
                  </div>
                </CardContent>
              </Card>

              <Card className="bg-gradient-card border-border">
                <CardContent className="p-4">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 bg-accent/20 rounded-lg flex items-center justify-center">
                      <BarChart3 className="w-5 h-5 text-accent" />
                    </div>
                    <div>
                      <p className="text-sm text-muted-foreground">Avg. Score</p>
                      <p className="text-2xl font-bold text-foreground">
                        {Math.round(researchResults.discoveredBuyers.reduce((acc, b) => acc + b.opportunityScore, 0) / researchResults.discoveredBuyers.length)}
                      </p>
                    </div>
                  </div>
                </CardContent>
              </Card>

              <Card className="bg-gradient-card border-border">
                <CardContent className="p-4">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 bg-primary/20 rounded-lg flex items-center justify-center">
                      <Globe className="w-5 h-5 text-primary" />
                    </div>
                    <div>
                      <p className="text-sm text-muted-foreground">Regions</p>
                      <p className="text-2xl font-bold text-foreground">
                        {new Set(researchResults.discoveredBuyers.map(b => b.country)).size}
                      </p>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>

            {/* UI Options Tabs */}
            <Card className="bg-gradient-card border-border">
              <CardHeader>
                <div className="flex items-center justify-between">
                  <CardTitle className="text-foreground">Discovered Buyers</CardTitle>
                  <Tabs value={activeUIOption} onValueChange={setActiveUIOption} className="w-auto">
                    <TabsList className="grid w-full grid-cols-3">
                      <TabsTrigger value="cards">Cards View</TabsTrigger>
                      <TabsTrigger value="table">Table View</TabsTrigger>
                      <TabsTrigger value="detailed">Detailed View</TabsTrigger>
                    </TabsList>
                  </Tabs>
                </div>
              </CardHeader>
              <CardContent>
                <Tabs value={activeUIOption} className="w-full">
                  {/* Cards View */}
                  <TabsContent value="cards" className="space-y-4 mt-0">
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                      {researchResults.discoveredBuyers.map((buyer) => (
                        <Card key={buyer.id} className="border-border hover:shadow-md transition-shadow">
                          <CardHeader className="pb-3">
                            <div className="flex items-start justify-between">
                              <div>
                                <h3 className="font-semibold text-foreground text-sm">{buyer.name}</h3>
                                <p className="text-xs text-muted-foreground">{buyer.country}</p>
                              </div>
                              <div className="flex items-center gap-1">
                                <Star className={`w-4 h-4 ${getOpportunityScoreColor(buyer.opportunityScore)}`} />
                                <span className={`text-sm font-medium ${getOpportunityScoreColor(buyer.opportunityScore)}`}>
                                  {buyer.opportunityScore}
                                </span>
                              </div>
                            </div>
                            <Badge className={`${getStatusColor(buyer.status)} text-white w-fit`}>
                              {buyer.status}
                            </Badge>
                          </CardHeader>
                          <CardContent className="pt-0 space-y-3">
                            <p className="text-xs text-muted-foreground">{buyer.targetSegment}</p>
                            <div className="space-y-1">
                              <h4 className="text-xs font-medium text-foreground">Key Contacts:</h4>
                              {buyer.keyContacts && buyer.keyContacts.slice(0, 2).map((contact, idx) => (
                                <p key={idx} className="text-xs text-muted-foreground">
                                  {contact.name || contact} - {contact.role || ''}
                                </p>
                              ))}
                            </div>
                            <div className="flex gap-2">
                              <Button 
                                size="sm" 
                                variant="outline" 
                                className="flex-1 text-xs"
                                onClick={() => {
                                  setSelectedBuyer(typeof buyer.id === 'string' ? parseInt(buyer.id) : buyer.id);
                                  setActiveUIOption("detailed");
                                }}
                              >
                                <Eye className="w-3 h-3 mr-1" />
                                View
                              </Button>
                              <Button 
                                size="sm" 
                                className="flex-1 text-xs"
                                onClick={() => window.open(buyer.website, '_blank')}
                              >
                                <ExternalLink className="w-3 h-3 mr-1" />
                                Visit
                              </Button>
                            </div>
                          </CardContent>
                        </Card>
                       ))}
                    </div>
                  </TabsContent>

                  {/* Table View */}
                  <TabsContent value="table" className="mt-0">
                    <Table>
                      <TableHeader>
                        <TableRow>
                          <TableHead>Company</TableHead>
                          <TableHead>Country/Region</TableHead>
                          <TableHead>Segment</TableHead>
                          <TableHead>Score</TableHead>
                          <TableHead>Status</TableHead>
                          <TableHead>Actions</TableHead>
                        </TableRow>
                      </TableHeader>
                      <TableBody>
                        {researchResults.discoveredBuyers.map((buyer) => (
                          <TableRow key={buyer.id}>
                            <TableCell>
                              <div>
                                <div className="font-medium">{buyer.name}</div>
                                <div className="text-sm text-muted-foreground">{buyer.website}</div>
                              </div>
                            </TableCell>
                            <TableCell>{buyer.country}</TableCell>
                            <TableCell className="max-w-[200px]">
                              <div className="truncate" title={buyer.targetSegment}>
                                {buyer.targetSegment}
                              </div>
                            </TableCell>
                            <TableCell>
                              <div className="flex items-center gap-1">
                                <Star className={`w-4 h-4 ${getOpportunityScoreColor(buyer.opportunityScore)}`} />
                                <span className={`font-medium ${getOpportunityScoreColor(buyer.opportunityScore)}`}>
                                  {buyer.opportunityScore}
                                </span>
                              </div>
                            </TableCell>
                            <TableCell>
                              <Badge className={`${getStatusColor(buyer.status)} text-white`}>
                                {buyer.status}
                              </Badge>
                            </TableCell>
                            <TableCell>
                              <div className="flex gap-2">
                                <Button 
                                  size="sm" 
                                  variant="outline"
                                  onClick={() => {
                                    setSelectedBuyer(typeof buyer.id === 'string' ? parseInt(buyer.id) : buyer.id);
                                    setActiveUIOption("detailed");
                                  }}
                                >
                                  <Eye className="w-4 h-4" />
                                </Button>
                                <Button 
                                  size="sm"
                                  onClick={() => window.open(buyer.website, '_blank')}
                                >
                                  <ExternalLink className="w-4 h-4" />
                                </Button>
                              </div>
                            </TableCell>
                          </TableRow>
                        ))}
                      </TableBody>
                    </Table>
                  </TabsContent>

                  {/* Detailed View */}
                  <TabsContent value="detailed" className="space-y-6 mt-0">
                    {researchResults.discoveredBuyers
                      .filter(buyer => selectedBuyer === null || (typeof buyer.id === 'string' ? parseInt(buyer.id) : buyer.id) === selectedBuyer)
                      .map((buyer) => (
                      <Card key={buyer.id} className="border-border">
                        <CardHeader>
                          <div className="flex items-start justify-between">
                            <div>
                              <h3 className="text-lg font-semibold text-foreground">{buyer.name}</h3>
                              <div className="flex items-center gap-4 mt-1">
                                <div className="flex items-center gap-1">
                                  <MapPin className="w-4 h-4 text-muted-foreground" />
                                  <span className="text-sm text-muted-foreground">{buyer.country} • {buyer.region || ''}</span>
                                </div>
                                <div className="flex items-center gap-1">
                                  <Globe className="w-4 h-4 text-muted-foreground" />
                                  <a href={buyer.website} target="_blank" rel="noopener noreferrer" 
                                     className="text-sm text-primary hover:underline">
                                    {buyer.website}
                                  </a>
                                </div>
                              </div>
                            </div>
                            <div className="flex items-center gap-3">
                              <div className="flex items-center gap-1">
                                <Star className={`w-5 h-5 ${getOpportunityScoreColor(buyer.opportunityScore)}`} />
                                <span className={`text-lg font-bold ${getOpportunityScoreColor(buyer.opportunityScore)}`}>
                                  {buyer.opportunityScore}
                                </span>
                              </div>
                              <Badge className={`${getStatusColor(buyer.status)} text-white`}>
                                {buyer.status}
                              </Badge>
                            </div>
                          </div>
                        </CardHeader>
                        <CardContent className="space-y-4">
                          <div>
                            <h4 className="font-medium text-foreground mb-2">Target Segment</h4>
                            <p className="text-sm text-muted-foreground">{buyer.targetSegment}</p>
                          </div>

                          {buyer.keyContacts && buyer.keyContacts.length > 0 && (
                            <div>
                              <h4 className="font-medium text-foreground mb-2">Key Contacts</h4>
                              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
                                {buyer.keyContacts.map((contact, idx) => (
                                  <div key={idx} className="border border-border rounded-lg p-3">
                                    {typeof contact === 'string' ? (
                                      <div className="font-medium text-sm">{contact}</div>
                                    ) : (
                                      <>
                                        <div className="font-medium text-sm">{contact.name}</div>
                                        <div className="text-xs text-muted-foreground">{contact.role}</div>
                                        {contact.email && (
                                          <div className="text-xs text-primary mt-1">{contact.email}</div>
                                        )}
                                      </>
                                    )}
                                  </div>
                                ))}
                              </div>
                            </div>
                          )}

                          {buyer.reasonForRecommendation && (
                            <div>
                              <h4 className="font-medium text-foreground mb-2">Recommendation Rationale</h4>
                              <p className="text-sm text-muted-foreground leading-relaxed">{buyer.reasonForRecommendation}</p>
                            </div>
                          )}

                          <div className="flex gap-3 pt-2">
                            <Button className="gap-2">
                              <MessageCircle className="w-4 h-4" />
                              Generate Outreach
                            </Button>
                            <Button variant="outline" className="gap-2">
                              <Eye className="w-4 h-4" />
                              View Full Profile
                            </Button>
                            <Button variant="outline" className="gap-2">
                              <ExternalLink className="w-4 h-4" />
                              Visit Website
                            </Button>
                          </div>
                        </CardContent>
                      </Card>
                    ))}
                  </TabsContent>
                </Tabs>
              </CardContent>
            </Card>
          </>
        )}
      </main>
    </div>
  );
};

export default BuyerDiscovery;
