import { Search, Filter, Mail, Phone, Building2, Calendar, MessageSquare, Download, User, Star } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";

const mockContacts = [
  {
    id: 1,
    name: "Dr. Sarah Chen",
    title: "Chief Procurement Officer",
    company: "MedCore Pharmaceuticals",
    location: "Berlin, Germany",
    email: "s.chen@medcore.com",
    phone: "+49 30 1234567",
    lastContact: "2 days ago",
    relationshipScore: 95,
    interactions: 23,
    tags: ["Decision Maker", "Strategic", "High Value"],
    department: "Procurement",
    seniority: "C-Level",
    recentActivity: "Attended PharmaTech Summit",
    notes: "Key decision maker for European procurement. Very responsive to innovative solutions."
  },
  {
    id: 2,
    name: "Marcus Rodriguez",
    title: "VP of Business Development",
    company: "BioPharma Solutions",
    location: "São Paulo, Brazil",
    email: "m.rodriguez@biopharma.com",
    phone: "+55 11 9876543",
    lastContact: "5 days ago",
    relationshipScore: 82,
    interactions: 18,
    tags: ["Influencer", "Partnership Focus"],
    department: "Business Development",
    seniority: "VP Level",
    recentActivity: "Signed partnership agreement",
    notes: "Excellent contact for Latin American expansion. Focus on strategic partnerships."
  },
  {
    id: 3,
    name: "Dr. Priya Sharma",
    title: "Head of Research",
    company: "Global Health Networks",
    location: "Mumbai, India",
    email: "p.sharma@globalhealth.in",
    phone: "+91 22 5555123",
    lastContact: "1 week ago",
    relationshipScore: 78,
    interactions: 15,
    tags: ["Technical Expert", "Research"],
    department: "R&D",
    seniority: "Director Level",
    recentActivity: "Published research paper",
    notes: "Leading expert in drug distribution networks. Values evidence-based approaches."
  },
  {
    id: 4,
    name: "James Mitchell",
    title: "Senior Director of Operations",
    company: "PharmaVision Corp",
    location: "Toronto, Canada",
    email: "j.mitchell@pharmavision.ca",
    phone: "+1 416 7778888",
    lastContact: "3 days ago",
    relationshipScore: 88,
    interactions: 31,
    tags: ["Operations", "Process Improvement"],
    department: "Operations",
    seniority: "Senior Director",
    recentActivity: "Implemented new supply chain system",
    notes: "Operations expert with focus on efficiency and cost optimization."
  }
];

const ContactIntelligence = () => {
  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b border-border bg-gradient-card shadow-card">
        <div className="flex h-16 items-center justify-between px-6">
          <div className="flex items-center gap-6">
            <h1 className="text-xl font-bold text-foreground">Contact Intelligence</h1>
            <div className="relative">
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-muted-foreground" />
              <Input 
                placeholder="Search contacts by name, company, title..." 
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
              Advanced Search
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
                  <User className="w-5 h-5 text-primary-foreground" />
                </div>
                <div>
                  <p className="text-sm text-muted-foreground">Total Contacts</p>
                  <p className="text-2xl font-bold text-foreground">8,942</p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-gradient-card border-border">
            <CardContent className="p-4">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-gradient-success rounded-lg flex items-center justify-center">
                  <Star className="w-5 h-5 text-success-foreground" />
                </div>
                <div>
                  <p className="text-sm text-muted-foreground">Key Contacts</p>
                  <p className="text-2xl font-bold text-foreground">234</p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-gradient-card border-border">
            <CardContent className="p-4">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-primary/20 rounded-lg flex items-center justify-center">
                  <MessageSquare className="w-5 h-5 text-primary" />
                </div>
                <div>
                  <p className="text-sm text-muted-foreground">Recent Interactions</p>
                  <p className="text-2xl font-bold text-foreground">1,847</p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-gradient-card border-border">
            <CardContent className="p-4">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-accent/20 rounded-lg flex items-center justify-center">
                  <Building2 className="w-5 h-5 text-accent" />
                </div>
                <div>
                  <p className="text-sm text-muted-foreground">Companies</p>
                  <p className="text-2xl font-bold text-foreground">1,203</p>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Filters */}
        <Card className="bg-gradient-card border-border">
          <CardHeader>
            <CardTitle className="text-foreground">Search & Filter Contacts</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
              <div>
                <label className="text-sm font-medium text-foreground mb-2 block">Department</label>
                <Select>
                  <SelectTrigger>
                    <SelectValue placeholder="All Departments" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="procurement">Procurement</SelectItem>
                    <SelectItem value="rd">Research & Development</SelectItem>
                    <SelectItem value="business">Business Development</SelectItem>
                    <SelectItem value="operations">Operations</SelectItem>
                    <SelectItem value="sales">Sales & Marketing</SelectItem>
                  </SelectContent>
                </Select>
              </div>
              <div>
                <label className="text-sm font-medium text-foreground mb-2 block">Seniority Level</label>
                <Select>
                  <SelectTrigger>
                    <SelectValue placeholder="All Levels" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="c-level">C-Level</SelectItem>
                    <SelectItem value="vp">VP Level</SelectItem>
                    <SelectItem value="director">Director</SelectItem>
                    <SelectItem value="manager">Manager</SelectItem>
                  </SelectContent>
                </Select>
              </div>
              <div>
                <label className="text-sm font-medium text-foreground mb-2 block">Relationship Score</label>
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
              <div>
                <label className="text-sm font-medium text-foreground mb-2 block">Last Contact</label>
                <Select>
                  <SelectTrigger>
                    <SelectValue placeholder="Any Time" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="week">Last Week</SelectItem>
                    <SelectItem value="month">Last Month</SelectItem>
                    <SelectItem value="quarter">Last Quarter</SelectItem>
                  </SelectContent>
                </Select>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Contact List */}
        <Card className="bg-gradient-card border-border">
          <CardHeader>
            <CardTitle className="text-foreground">Contact Directory</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              {mockContacts.map((contact) => (
                <div key={contact.id} className="border border-border rounded-lg p-4 hover:bg-muted/20 transition-colors">
                  <div className="flex items-start gap-4">
                    <Avatar className="w-12 h-12">
                      <AvatarFallback className="bg-gradient-primary text-primary-foreground">
                        {contact.name.split(' ').map(n => n[0]).join('')}
                      </AvatarFallback>
                    </Avatar>

                    <div className="flex-1">
                      <div className="flex items-center gap-3 mb-2">
                        <h3 className="font-semibold text-foreground text-lg">{contact.name}</h3>
                        <div className="flex items-center gap-1">
                          <Star className="w-4 h-4 text-warning fill-warning" />
                          <span className="text-sm font-medium text-foreground">
                            {contact.relationshipScore}%
                          </span>
                        </div>
                      </div>
                      
                      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-3">
                        <div>
                          <p className="text-sm font-medium text-foreground">{contact.title}</p>
                          <p className="text-sm text-muted-foreground">{contact.company}</p>
                          <p className="text-xs text-muted-foreground">{contact.location}</p>
                        </div>
                        <div>
                          <div className="flex items-center gap-2 mb-1">
                            <Mail className="w-3 h-3 text-muted-foreground" />
                            <span className="text-xs text-muted-foreground">{contact.email}</span>
                          </div>
                          <div className="flex items-center gap-2">
                            <Phone className="w-3 h-3 text-muted-foreground" />
                            <span className="text-xs text-muted-foreground">{contact.phone}</span>
                          </div>
                        </div>
                      </div>

                      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-3">
                        <div>
                          <span className="text-xs text-muted-foreground">Department: </span>
                          <span className="text-xs font-medium text-foreground">{contact.department}</span>
                        </div>
                        <div>
                          <span className="text-xs text-muted-foreground">Interactions: </span>
                          <span className="text-xs font-medium text-foreground">{contact.interactions}</span>
                        </div>
                        <div>
                          <span className="text-xs text-muted-foreground">Last Contact: </span>
                          <span className="text-xs font-medium text-foreground">{contact.lastContact}</span>
                        </div>
                      </div>

                      <div className="mb-3">
                        <div className="flex flex-wrap gap-1">
                          {contact.tags.map((tag, index) => (
                            <Badge key={index} variant="outline" className="text-xs">
                              {tag}
                            </Badge>
                          ))}
                        </div>
                      </div>

                      <div className="text-xs text-muted-foreground mb-2">
                        <strong>Recent Activity:</strong> {contact.recentActivity}
                      </div>

                      <div className="text-xs text-muted-foreground italic">
                        "{contact.notes}"
                      </div>
                    </div>

                    <div className="flex flex-col gap-2">
                      <Button size="sm" className="gap-2">
                        <Mail className="w-4 h-4" />
                        Contact
                      </Button>
                      <Button variant="outline" size="sm" className="gap-2">
                        <Calendar className="w-4 h-4" />
                        Schedule
                      </Button>
                      <Button variant="outline" size="sm" className="gap-2">
                        <MessageSquare className="w-4 h-4" />
                        History
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

export default ContactIntelligence;