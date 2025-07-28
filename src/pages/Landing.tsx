import { useState } from "react";
import { Link } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { 
  BarChart3, 
  Globe, 
  Users, 
  Search, 
  TrendingUp,
  ChevronRight,
  PlayCircle,
  CheckCircle
} from "lucide-react";

const Landing = () => {
  const [activeFeature, setActiveFeature] = useState(0);

  const features = [
    {
      icon: BarChart3,
      title: "Market Intelligence Dashboard",
      description: "Real-time insights into global pharmaceutical trade flows, emerging trends, and market opportunities.",
      benefit: "Stay ahead of market shifts with comprehensive data visualization"
    },
    {
      icon: Search,
      title: "Buyer Discovery Engine",
      description: "AI-powered prospect identification that finds the most relevant buyers for your pharmaceutical products.",
      benefit: "Reduce prospecting time from weeks to minutes"
    },
    {
      icon: Users,
      title: "Contact Intelligence",
      description: "Automated discovery of key decision-makers and stakeholders within target pharmaceutical companies.",
      benefit: "Connect directly with the right people at the right companies"
    }
  ];

  const steps = [
    {
      step: "01",
      title: "Data Aggregation",
      description: "We continuously collect and harmonize global pharmaceutical trade data, company registries, and regulatory databases."
    },
    {
      step: "02", 
      title: "AI Analysis",
      description: "Our machine learning algorithms analyze patterns, identify opportunities, and score potential business matches."
    },
    {
      step: "03",
      title: "Smart Recommendations",
      description: "Get actionable insights with ranked prospects, contact information, and suggested outreach strategies."
    }
  ];

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b border-border/40">
        <div className="container mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-2">
              <div className="w-8 h-8 bg-gradient-to-br from-primary to-primary-glow rounded-lg flex items-center justify-center">
                <BarChart3 className="w-5 h-5 text-white" />
              </div>
              <span className="text-xl font-bold bg-gradient-to-r from-primary to-primary-glow bg-clip-text text-transparent">
                PharmaSage
              </span>
            </div>
            
            <nav className="hidden md:flex items-center space-x-6">
              <a href="#features" className="text-muted-foreground hover:text-foreground transition-colors">How it works?</a>
              <a href="#pricing" className="text-muted-foreground hover:text-foreground transition-colors">Pricing</a>
              <Link to="/dashboard">
                <Button variant="outline" size="sm">View Dashboard</Button>
              </Link>
            </nav>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-br from-primary/5 via-background to-accent/5" />
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_30%_40%,hsl(var(--primary))_0%,transparent_50%)] opacity-10" />
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_70%_80%,hsl(var(--accent))_0%,transparent_50%)] opacity-10" />
        
        <div className="relative container mx-auto px-6 py-24">
          <div className="max-w-4xl">
            <div className="inline-flex items-center space-x-2 bg-primary/10 border border-primary/20 rounded-full px-4 py-2 mb-8">
              <div className="w-2 h-2 bg-primary rounded-full animate-pulse" />
              <span className="text-sm text-primary font-medium">Next-Gen Pharma Intelligence</span>
            </div>
            
            <h1 className="text-5xl md:text-6xl font-bold mb-6 leading-tight">
              Smarter Pharma Business Intelligence{" "}
              <span className="bg-gradient-to-r from-primary to-primary-glow bg-clip-text text-transparent">
                Starts Here
              </span>
            </h1>
            
            <p className="text-xl text-muted-foreground mb-8 max-w-2xl leading-relaxed">
              Discover global market opportunities, identify qualified buyers, and accelerate pharmaceutical business development with AI-powered intelligence.
            </p>
            
            <div className="flex justify-start">
              <a href="#features">
                <Button size="lg" className="bg-gradient-to-r from-primary to-primary-glow hover:from-primary/90 hover:to-primary-glow/90 text-white shadow-lg hover:shadow-primary/25 transition-all duration-300">
                  <PlayCircle className="w-5 h-5 mr-2" />
                  How it works?
                </Button>
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-24 bg-muted/30">
        <div className="container mx-auto px-6">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-4">
              Comprehensive Pharma Intelligence Suite
            </h2>
            <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
              Everything you need to identify opportunities, find buyers, and accelerate growth in global pharmaceutical markets.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <Link to="/dashboard">
              <Card 
                className={`group cursor-pointer transition-all duration-300 hover:shadow-lg hover:shadow-primary/10 border-border/50 ${
                  activeFeature === 0 ? 'border-primary/40 bg-primary/5' : ''
                }`}
                onMouseEnter={() => setActiveFeature(0)}
              >
                <CardHeader className="pb-4">
                  <div className={`w-12 h-12 rounded-lg flex items-center justify-center mb-4 transition-colors ${
                    activeFeature === 0 
                      ? 'bg-gradient-to-br from-primary to-primary-glow text-white' 
                      : 'bg-muted group-hover:bg-primary/10'
                  }`}>
                    <BarChart3 className="w-6 h-6" />
                  </div>
                  <CardTitle className="text-lg">Market Intelligence Dashboard</CardTitle>
                </CardHeader>
                <CardContent className="pt-0">
                  <CardDescription className="mb-3">Real-time insights into global pharmaceutical trade flows, emerging trends, and market opportunities.</CardDescription>
                  <div className="text-sm text-primary font-medium">Stay ahead of market shifts with comprehensive data visualization</div>
                </CardContent>
              </Card>
            </Link>

            <Link to="/buyer-discovery">
              <Card 
                className={`group cursor-pointer transition-all duration-300 hover:shadow-lg hover:shadow-primary/10 border-border/50 ${
                  activeFeature === 1 ? 'border-primary/40 bg-primary/5' : ''
                }`}
                onMouseEnter={() => setActiveFeature(1)}
              >
                <CardHeader className="pb-4">
                  <div className={`w-12 h-12 rounded-lg flex items-center justify-center mb-4 transition-colors ${
                    activeFeature === 1 
                      ? 'bg-gradient-to-br from-primary to-primary-glow text-white' 
                      : 'bg-muted group-hover:bg-primary/10'
                  }`}>
                    <Search className="w-6 h-6" />
                  </div>
                  <CardTitle className="text-lg">Buyer Discovery Engine</CardTitle>
                </CardHeader>
                <CardContent className="pt-0">
                  <CardDescription className="mb-3">AI-powered prospect identification that finds the most relevant buyers for your pharmaceutical products.</CardDescription>
                  <div className="text-sm text-primary font-medium">Reduce prospecting time from weeks to minutes</div>
                </CardContent>
              </Card>
            </Link>

            <Link to="/contact-intelligence">
              <Card 
                className={`group cursor-pointer transition-all duration-300 hover:shadow-lg hover:shadow-primary/10 border-border/50 ${
                  activeFeature === 2 ? 'border-primary/40 bg-primary/5' : ''
                }`}
                onMouseEnter={() => setActiveFeature(2)}
              >
                <CardHeader className="pb-4">
                  <div className={`w-12 h-12 rounded-lg flex items-center justify-center mb-4 transition-colors ${
                    activeFeature === 2 
                      ? 'bg-gradient-to-br from-primary to-primary-glow text-white' 
                      : 'bg-muted group-hover:bg-primary/10'
                  }`}>
                    <Users className="w-6 h-6" />
                  </div>
                  <CardTitle className="text-lg">Contact Intelligence</CardTitle>
                </CardHeader>
                <CardContent className="pt-0">
                  <CardDescription className="mb-3">Automated discovery of key decision-makers and stakeholders within target pharmaceutical companies.</CardDescription>
                  <div className="text-sm text-primary font-medium">Connect directly with the right people at the right companies</div>
                </CardContent>
              </Card>
            </Link>
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section id="how-it-works" className="py-24">
        <div className="container mx-auto px-6">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-4">How PharmaSage Works</h2>
            <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
              An end-to-end AI stack that transforms pharmaceutical business intelligence from manual research to automated insights.
            </p>
          </div>

          <div className="max-w-4xl mx-auto">
            {steps.map((step, index) => (
              <div key={index} className="flex items-start space-x-6 mb-12 last:mb-0">
                <div className="flex-shrink-0">
                  <div className="w-16 h-16 bg-gradient-to-br from-primary to-primary-glow rounded-full flex items-center justify-center text-white font-bold text-lg shadow-lg">
                    {step.step}
                  </div>
                </div>
                <div className="flex-1">
                  <h3 className="text-xl font-semibold mb-2">{step.title}</h3>
                  <p className="text-muted-foreground text-lg leading-relaxed">{step.description}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-24 bg-gradient-to-br from-primary/5 via-background to-accent/5">
        <div className="container mx-auto px-6 text-center">
          <div className="max-w-3xl mx-auto">
            <h2 className="text-3xl md:text-4xl font-bold mb-6">
              Ready to Transform Your Pharma Intelligence?
            </h2>
            <p className="text-lg text-muted-foreground mb-8">
              Join leading pharmaceutical companies using PharmaSage to discover opportunities and accelerate growth.
            </p>
            
            <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
              <Link to="/dashboard">
                <Button size="lg" className="bg-gradient-to-r from-primary to-primary-glow hover:from-primary/90 hover:to-primary-glow/90 text-white shadow-lg hover:shadow-primary/25 transition-all duration-300">
                  <BarChart3 className="w-5 h-5 mr-2" />
                  Access InsightGrid Dashboard
                  <ChevronRight className="w-4 h-4 ml-2" />
                </Button>
              </Link>
            </div>

            <div className="flex items-center justify-center space-x-6 mt-8 text-sm text-muted-foreground">
              <div className="flex items-center space-x-2">
                <CheckCircle className="w-4 h-4 text-primary" />
                <span>Real-time data</span>
              </div>
              <div className="flex items-center space-x-2">
                <CheckCircle className="w-4 h-4 text-primary" />
                <span>AI-powered insights</span>
              </div>
              <div className="flex items-center space-x-2">
                <CheckCircle className="w-4 h-4 text-primary" />
                <span>Global coverage</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-border/40 py-12 bg-muted/30">
        <div className="container mx-auto px-6">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <div className="flex items-center space-x-2 mb-4 md:mb-0">
              <div className="w-6 h-6 bg-gradient-to-br from-primary to-primary-glow rounded flex items-center justify-center">
                <BarChart3 className="w-4 h-4 text-white" />
              </div>
              <span className="font-bold bg-gradient-to-r from-primary to-primary-glow bg-clip-text text-transparent">
                PharmaSage
              </span>
            </div>
            <div className="text-sm text-muted-foreground">
              © 2024 PharmaSage. Intelligent pharmaceutical business intelligence.
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default Landing;
